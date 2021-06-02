from django.shortcuts import render, redirect , HttpResponse
import math 
from django.contrib import messages
# Create your views here.
def home(request):
    return redirect('/physics-calculator/')

def calc1(request):
    try:
        Given = request.POST.get('Given','form1')
        m = request.POST.get('m')
        v = request.POST.get('v')
        ke = request.POST.get('ke')
        def velconverter(t,l):
            if t == "km/s":
                l = l * 1000
            elif t == "mi/s":
                l = l * 1609
            elif t == "c":
                l = l * 299792458
            elif t == "km/h":
                l = l * 5/18
            elif t == "ft/s":
                l = l * 0.3048
            elif t == "mi/h":
                l = l * 0.44704
            elif t == "knots":
                l = l  * 0.514444
            return l
        def massconverter(t,l):
            if t == "ug":
                l= l /1000000000
            elif t == "mg":
                l= l / 1000000
            elif t == "g":
                l = l /1000
            elif t == "dag":
                l =l * 0.01
            elif t == "t":
                l = l * 1000
            elif t == "gr":
                l = l / 15432
            elif t == "dr":
                l = l * 0.0018
            elif t == "oz":
                l = l / 35.274
            elif t == "ib":
                l = l * 0.45359237
            elif t == "stone":
                l = l * 6.35029
            elif t == "uston":
                l = l * 907.185
            elif t == "longton":
                l = l * 1016.05
            elif t == "me":
                l = l /9.223e+18
            elif t == "u":
                l = l  / 9.223e+18
            return l

        def keconverter(t,l):
            if t == "kj":
                l = l *1000
            elif t == "mj":
                l = l * 1000000
            elif t == "wh":
                l = l * 3600
            elif t =="kwh":
                l = l * 3.6000000
            elif t == "ft-lbs":
                l = l * 1.356
            elif t == "kcal":
                l = l * 4184
            elif t == "ev":
                l = l * 6.242e+18
            return l   
        if request.method == "POST":
            if Given == "form1" and v and m:
                m = float(request.POST.get('m'))
                v = float(request.POST.get('v'))
                m_op = request.POST.get('m_op')
                v_op = request.POST.get('v_op')
                c=299792458
                vm = velconverter(v_op,v)
                mm = massconverter(m_op,m)

                mo = mm / (math.sqrt(1-vm**2/c**2))
                ke = mo*(c**2)*(math.sqrt(1-vm**2/c**2)-1)
                
                if mm<0:
                    ke = -ke
                else:
                    ke = abs(ke)
                
                redict = {'J':ke,'KJ':ke/1000,'MJ':ke/1e+6,'Wh':ke/3600,'Kwh':ke/6e+6,'ft-lbs':ke/1.356,'Kcal':ke/4184,'eV':ke*6.242e+18
    }
                context = {
                'm':m,
                'mm':mm,
                'mo':mo,
                'v':v,
                'vm':vm,
                'm_op':m_op,
                'v_op':v_op,
                'result':ke,
                'Given':Given,
                'redict':redict
                }
                return render(request,'calc/calc.html',context)
            elif Given == "form2" and ke and m:
                m = float(request.POST.get('m'))
                ke = float(request.POST.get('ke'))
                m_op = request.POST.get('m_op')
                ke_op = request.POST.get('ke_op')
                kem = keconverter(ke_op,ke)
                mm = massconverter(m_op,m)

                v = math.sqrt(ke/(1/2*m))
                
                redict = {"m/s":v,"km/h":v/3.6,"ft/s":v*3.281,"mi/h":v*2.237,"knots":v*1.944,"km/s":v/1000,"mi/s":v/1609,"light Speed(c)":v/2.998e+8
    }
                context = {
                'm':m,
                'mm':mm,
                'ke':ke,
                'kem':kem,
                'm_op':m_op,
                'ke_op':ke_op,
                'result':v,
                'Given':Given,
                'redict':redict
                }
                return render(request,'calc/calc.html',context)

            elif Given == "form3" and ke and v:
                v = float(request.POST.get('v'))
                ke = float(request.POST.get('ke'))
                v_op = request.POST.get('v_op')
                ke_op = request.POST.get('ke_op')
                kem = keconverter(ke_op,ke)
                vm = velconverter(v_op,v)

                m = (2*kem)/vm**2
                
                redict = {"Micrograms(ug)":m*1e+9,"Milligrams(mg)":m*1e+6,"Grams(g)":m*1000,"Decagrams(dag)":m*100,"Metric tons(t)":m/1000,"Grains(gr)":m*15432,"Drachms(dr)":m*564.38,"Ounces(oz)":m*35.274,"Pounds(lb)":m*2.205,"Stone":m/6.35,"US short ton(US ton)":m/907,"Imperial ton(long ton)":m/1016,"Electron rest mass(me)":m*9.223e+18,"Atomic mass unit(u)":m/9.223e+18}
                context = {
                'vm':vm,
                'v':v,
                'ke':ke,
                'kem':kem,
                'v_op':v_op,
                'ke_op':ke_op,
                'result':m,
                'Given':Given,
                'redict':redict
                }
                return render(request,'calc/calc.html',context)
                
            return render(request,'calc/calc.html',{'Given':Given})
        return render(request,'calc/calc.html',{'Given':Given})
    except:
        messages.error(request,"Please enter vaild data")
        return render(request,'calc/calc.html',{'Given':'form1'})
