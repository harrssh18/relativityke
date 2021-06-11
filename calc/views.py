from django.shortcuts import render, redirect , HttpResponse
import math 
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'calc/home.html')


#relativistic kinetic energy
def relativistic(request):
    try:
        Given = request.POST.get('Given','form1')
        m = request.POST.get('m')
        v = request.POST.get('v')
        ke = request.POST.get('ke')
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
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
                
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(ke)
                if 'e' in str(ke):
                    r11 = str(ke)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                    
                elif count>5:
                    r11 = str("{:.2e}".format(ke))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                    
                redict = {'J':ke,'KJ':ke/1000,'MJ':ke/1e+6,'Wh':ke/3600,'Kwh':ke/6e+6,'ft-lbs':ke/1.356,'Kcal':ke/4184,'eV':ke*6.242e+18
    }
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
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
                return render(request,'calc/relativistic.html',context)
            elif Given == "form2" and ke and m:
                m = float(request.POST.get('m'))
                ke = float(request.POST.get('ke'))
                m_op = request.POST.get('m_op')
                ke_op = request.POST.get('ke_op')
                kem = keconverter(ke_op,ke)
                mm = massconverter(m_op,m)

                v = math.sqrt(ke/(1/2*m))
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(v)
                if str(v) in 'e':
                    index_num = v.index('e')
                    stratpoint = v[:index_num]
                    endpoint = v[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(v))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {"m/s":v,"km/h":v/3.6,"ft/s":v*3.281,"mi/h":v*2.237,"knots":v*1.944,"km/s":v/1000,"mi/s":v/1609,"light Speed(c)":v/2.998e+8
    }
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
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
                return render(request,'calc/relativistic.html',context)

            elif Given == "form3" and ke and v:
                v = float(request.POST.get('v'))
                ke = float(request.POST.get('ke'))
                v_op = request.POST.get('v_op')
                ke_op = request.POST.get('ke_op')
                kem = keconverter(ke_op,ke)
                vm = velconverter(v_op,v)

                m = (2*kem)/vm**2
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(m)
                if str(m) in 'e':
                    r11 = str(m)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(m))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {"Micrograms(ug)":m*1e+9,"Milligrams(mg)":m*1e+6,"Grams(g)":m*1000,"Decagrams(dag)":m*100,"Metric tons(t)":m/1000,"Grains(gr)":m*15432,"Drachms(dr)":m*564.38,"Ounces(oz)":m*35.274,"Pounds(lb)":m*2.205,"Stone":m/6.35,"US short ton(US ton)":m/907,"Imperial ton(long ton)":m/1016,"Electron rest mass(me)":m*9.223e+18,"Atomic mass unit(u)":m/9.223e+18}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
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
                return render(request,'calc/relativistic.html',context)
                
            return render(request,'calc/relativistic.html',{'Given':Given})
        return render(request,'calc/relativistic.html',{'Given':Given})
    except:
        messages.error(request,"Please enter vaild data")
        return render(request,'calc/relativistic.html',{'Given':'form1'})

#compton scattering calc
def compton_scattering(request):
    try:

        Given = request.POST.get('Given','form1')
        sa = request.POST.get('sa')
        w = request.POST.get('w')
        m = request.POST.get('m')
        h = 6.62607 * (10**-34) 
        c = 299792458
        pi = 3.14
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        def massconverter(t,l):
            if t == "ug":
                l=l/1e+9
            elif t == "mg":
                l=l/1e+6
            elif t == "g":
                l=l/1000
            elif t=="dag":
                l=l/100
            elif t == "me":
                l=l/9.223e+18
            return l
        def meterconverter(t,l):
            if t == "A":
                l=l/1e+10
            elif t == "pm":
                l=l/1e+12
            elif t == "nm":
                l=l/1e+9
            elif t=="um":
                l=l/1e+6
            elif t == "mm":
                l=l/1000
            elif t == "cm":
                l=l/100
            return l
        def angleconverter(t,l):
            pi = 3.14
            if t == "deg":
                l=l*(pi/180)
            elif t == "gon":
                l=l*(pi/200)
            elif t == "tr":
                l=l*(2*pi)
            elif t=="arcmin":
                l=l*pi*(60*180)
            elif t == "arcsec":
                l=l/(180*3600)
            elif t == "mrad":
                l=l/1000
            elif t == "urad":
                l=l*0.0000001
            return l
        if request.method == "POST":
            if Given == "form3" and m and sa:
                sa_op = request.POST.get('sa_op')
                m_op = request.POST.get('m_op')
                sa = float(request.POST.get('sa'))
                m = float(request.POST.get('m'))
                sam = angleconverter(sa_op,sa)
                mm = massconverter(m_op,m)

                re = h / (mm * c) * (1 - math.cos(sam))
                
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if 'e' in str(re):
                    r11 = str(re)
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Angstrom (A)':re*1e+10,'PicoMeters (pm)':re*1e+12,'NanoMeters (nm)':re*1e+9,'MicroMeter (mm)':re*1e+6,'MilliMeter (um)':re*100,'CentiMeter (cm)':re*100,'Meter (m)':re}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'Given':Given,
                'sa':sa,
                'sam':sam,
                'm':m,
                'mm':mm,
                'm_op':m_op,
                'sa_op':sa_op,
                'result':re,
                'redict':redict,
                'c':c
                }
                return render(request,'calc/compton_scattering.html',context)
            elif Given == "form2" and m and w:
                w_op = request.POST.get('w_op')
                m_op = request.POST.get('m_op')
                w = float(request.POST.get('w'))
                m = float(request.POST.get('m'))
                wm = meterconverter(w_op,w)
                mm = massconverter(m_op,m)

                re = 1 - (wm*mm*c)/h
                
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if 'e' in str(re):
                    r11 = str(re)
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Radians (Rad)':re,'Degrees (deg)':re*(180/pi),'Gradians (gon)':re*(200/pi),'Turns (tr)':re/(2*pi),'Minute of Arc (arcmin)':re * ((60 * 180)/pi),'Second of Arc (arcsec)':re*( (3600 * 180)/pi),'MilliRadian (mrad)':re*1000,'MicroRadian (urad)':re*1000000}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'Given':Given,
                'w':w,
                'wm':wm,
                'm':m,
                'mm':mm,
                'm_op':m_op,
                'w_op':w_op,
                'result':re,
                'redict':redict,
                'c':c
                }
                return render(request,'calc/compton_scattering.html',context)

            elif Given == "form1" and sa and w:
                w_op = request.POST.get('w_op')
                sa_op = request.POST.get('sa_op')
                w = float(request.POST.get('w'))
                sa = float(request.POST.get('sa'))
                wm = meterconverter(w_op,w)
                sam = angleconverter(sa_op,sa)

                re = h / wm * (1- math.cos(sam))
                
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if 'e' in str(re):
                    r11 = str(re)
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Microgram (ug)':re*1e+9,'Milligram (mm)':re*1e+6,'Grams (g)':re*1000,'Decagrams':re*100,'Kilogram':re,'Electron rest mass (me)':re* 9.223e+18}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'Given':Given,
                'w':w,
                'wm':wm,
                'sa':sa,
                'sam':sam,
                'w_op':w_op,
                'sa_op':sa_op,
                'result':re,
                'redict':redict,
                'c':c
                }
                return render(request,'calc/compton_scattering.html',context)
            return render(request,'calc/compton_scattering.html',{'Given':Given})
        else:
            return render(request,'calc/compton_scattering.html',{'Given':Given})
    except:
        messages.error(request,'Please Enter Valid Data')
        return render(request,'calc/compton_scattering.html',{'Given':'form1'})

#wattstoamps calc
def wattstoamps(request):
    try:
        ctype = request.POST.get('ctype','form1')
        ttype = request.POST.get('ttype','form1')
        a = request.POST.get('a')
        v = request.POST.get('v')
        p = request.POST.get('p')
        pf = request.POST.get('pf')
        vtype = request.POST.get('vtype','form1')
        def wattconverter(t,l):
            if t == 'mW':
                l = l / 1000
            elif t == 'kW':
                l = l * 1000
            elif t== 'MW':
                l = l * 1000000
            elif t == 'GW':
                l = l * 1000000000
            elif t == 'btu/h':
                l = l / 3.41
            elif t == 'hp(E)':
                l = l * 746
            return l
        def voltconverter(t,l):
            if t == 'kV':
                l = l * 1000
            elif t == 'mV':
                l = l / 1000
            elif t== 'MV':
                l = l * 1000000
            return l
        def ampereconverter(t,l):
            if t == 'mA':
                l = l / 1000
            elif t == 'uA':
                l = l * 1000000
            return l
        def zerocount(v):
                l = str(v).count('0')
                return int(l)
        if request.method == 'POST':
            if ctype == 'form1' and ttype == 'form1' and v and p:
                ctype = request.POST['ctype']
                p = float(request.POST['p'])
                v = float(request.POST['v'])
                p_op = request.POST['p_op']
                v_op = request.POST['v_op']

                pw = wattconverter(p_op,p)
                vw = voltconverter(v_op,v)

                re = pw / vw
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                
                redict = {'Ampere (A)':re,'MilliAmpere (mA)':re * 1000,'MicroAmpere (uA)': re*1000000}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'p':p,
                'v':v,
                'p_op':p_op,
                'v_op':v_op,
                'pw':pw,
                'vw':vw,
                'result':re,
                'redict':redict,
                'ctype':ctype,
                'ttype':ttype
                }
                return render(request,'calc/wattstoamps.html',context)
            elif ctype == 'form1' and ttype == 'form2' and v and a:
                ctype = request.POST['ctype']
                a = float(request.POST['a'])
                v = float(request.POST['v'])
                a_op = request.POST['a_op']
                v_op = request.POST['v_op']

                aw = ampereconverter(a_op,a)
                vw = voltconverter(v_op,v)

                re = aw * vw
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Watts (W)':re,'MilliWatts (mW)':re * 1000,'MegaWatts (MW)': re/1000000,'KiloWatts (kW)':re/1000,'GigaWatts (GW)':re/1000000000,'British Thermal Unit per hour (BTU/h)':re*3.412141633,'Electric horse Power (hp(E))':re/746}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'a':a,
                'v':v,
                'a_op':a_op,
                'v_op':v_op,
                'vw':vw,
                'aw':aw,
                'result':re,
                'redict':redict,
                'ctype':ctype,
                'ttype':ttype
                }
                return render(request,'calc/wattstoamps.html',context)
            elif ctype == 'form1' and ttype == 'form3' and p and a:
                ctype = request.POST['ctype']
                a = float(request.POST['a'])
                p = float(request.POST['p'])
                a_op = request.POST['a_op']
                p_op = request.POST['p_op']

                aw = ampereconverter(a_op,a)
                pw = wattconverter(p_op,p)

                re = pw / aw
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Volts (V)':re,'MilliVolts (mV)':re * 1000,'MegaVolts (MV)': re/1000000,'KiloVolts (kV)':re/1000}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'a':a,
                'p':p,
                'a_op':a_op,
                'p_op':p_op,
                'pw':pw,
                'aw':aw,
                'result':re,
                'redict':redict,
                'ctype':ctype,
                'ttype':ttype
                }
                return render(request,'calc/wattstoamps.html',context)
            elif ctype == 'form2' and ttype == 'form1' and p and v and pf:
                ctype = request.POST['ctype']
                v = float(request.POST['v'])
                p = float(request.POST['p'])
                pf = float(request.POST['pf'])
                v_op = request.POST['v_op']
                p_op = request.POST['p_op']

                vw = voltconverter(v_op,v)
                pw = wattconverter(p_op,p)

                re = pw * ( vw * pf)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Ampere (A)':re,'MilliAmpere (mA)':re * 1000,'MicroAmpere (uA)': re*1000000}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'v':v,
                'p':p,
                'pf':pf,
                'v_op':v_op,
                'p_op':p_op,
                'pw':pw,
                'vw':vw,
                'result':re,
                'redict':redict,
                'ctype':ctype,
                'ttype':ttype
                }
                return render(request,'calc/wattstoamps.html',context)
            elif ctype == 'form2' and ttype == 'form2' and a and v and pf:
                ctype = request.POST['ctype']
                v = float(request.POST['v'])
                a = float(request.POST['a'])
                pf = float(request.POST['pf'])
                v_op = request.POST['v_op']
                a_op = request.POST['a_op']

                vw = voltconverter(v_op,v)
                aw = ampereconverter(a_op,a)

                re = vw *(aw * pf)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Watts (W)':re,'MilliWatts (mW)':re * 1000,'MegaWatts (MW)': re/1000000,'KiloWatts (kW)':re/1000,'GigaWatts (GW)':re/1000000000,'British Thermal Unit per hour (BTU/h)':re*3.412141633,'Electric horse Power (hp(E))':re/746}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'v':v,
                'a':a,
                'pf':pf,
                'v_op':v_op,
                'a_op':a_op,
                'aw':aw,
                'vw':vw,
                'result':re,
                'redict':redict,
                'ctype':ctype,
                'ttype':ttype
                }
                return render(request,'calc/wattstoamps.html',context)
            elif ctype == 'form2' and ttype == 'form3' and a and p and pf:
                ctype = request.POST['ctype']
                p = float(request.POST['p'])
                a = float(request.POST['a'])
                pf = float(request.POST['pf'])
                p_op = request.POST['p_op']
                a_op = request.POST['a_op']

                pw = wattconverter(p_op,p)
                aw = ampereconverter(a_op,a)

                re = pw / (aw * pf) 
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Watts (W)':re,'MilliWatts (mW)':re * 1000,'MegaWatts (MW)': re/1000000,'KiloWatts (kW)':re/1000,'GigaWatts (GW)':re/1000000000,'British Thermal Unit per hour (BTU/h)':re*3.412141633,'Electric horse Power (hp(E))':re/746}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'p':p,
                'a':a,
                'pf':pf,
                'p_op':p_op,
                'a_op':a_op,
                'aw':aw,
                'pw':pw,
                'result':re,
                'redict':redict,
                'ctype':ctype,
                'ttype':ttype
                }
                return render(request,'calc/wattstoamps.html',context)
            elif ctype == 'form2' and ttype == 'form4' and a and p and v:
                ctype = request.POST['ctype']
                p = float(request.POST['p'])
                a = float(request.POST['a'])
                v = float(request.POST['v'])
                p_op = request.POST['p_op']
                a_op = request.POST['a_op']
                v_op = request.POST['v_op']

                pw = wattconverter(p_op,p)
                aw = ampereconverter(a_op,a)
                vw = voltconverter(v_op,v)

                re = (pw / vw) / aw 
                
                context = {
                'p':p,
                'a':a,
                'v':v,
                'v_op':v_op,
                'p_op':p_op,
                'a_op':a_op,
                'vw':vw,
                'aw':aw,
                'pw':pw,
                'result':re,
                'ctype':ctype,
                'ttype':ttype
                }
                return render(request,'calc/wattstoamps.html',context)
            elif ctype == 'form3' and ttype == 'form1' and pf and p and v and vtype:
                ctype = request.POST['ctype']
                vtype = request.POST['vtype']
                p = float(request.POST['p'])
                pf = float(request.POST['pf'])
                v = float(request.POST['v'])
                p_op = request.POST['p_op']
                v_op = request.POST['v_op']

                pw = wattconverter(p_op,p)
                vw = voltconverter(v_op,v)

                if vtype == 'form1':
                    re =  pw / (math.sqrt(3) * vw * pf)
                    formula = "P / (√3 * V * PF)"
                    f = True
                else:
                    re =  pw / (3 * vw * pf)
                    formula = "P / (3 * V * PF)"
                    f = False
               
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Ampere (A)':re,'MilliAmpere (mA)':re * 1000,'MicroAmpere (uA)': re*1000000}
                context = {
                'f':f,
                'formula':formula,
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'p':p,
                'pf':pf,
                'v':v,
                'v_op':v_op,
                'p_op':p_op,
                'vw':vw,
                'pw':pw,
                'result':re,
                'redict':redict,
                'ctype':ctype,
                'ttype':ttype,
                'vtype':vtype
                }
                return render(request,'calc/wattstoamps.html',context)

            elif ctype == 'form3' and ttype == 'form2' and pf and a and v and vtype:
                ctype = request.POST['ctype']
                vtype = request.POST['vtype']
                a = float(request.POST['a'])
                pf = float(request.POST['pf'])
                v = float(request.POST['v'])
                a_op = request.POST['a_op']
                v_op = request.POST['v_op']

                aw = ampereconverter(a_op,a)
                vw = voltconverter(v_op,v)

                if vtype == 'form1':
                    re =  (math.sqrt(3) * vw * pf) * aw
                    formula = "(√3 * V * PF) * I"
                    f = True
                else:
                    re =  (3 * vw * pf) * aw
                    formula = "(3 * V * PF) * I"
                    f = False
                
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Watts (W)':re,'MilliWatts (mW)':re * 1000,'MegaWatts (MW)': re/1000000,'KiloWatts (kW)':re/1000,'GigaWatts (GW)':re/1000000000,'British Thermal Unit per hour (BTU/h)':re*3.412141633,'Electric horse Power (hp(E))':re/746}
                context = {
                'f':f,
                'formula':formula,
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'a':a,
                'pf':pf,
                'v':v,
                'v_op':v_op,
                'a_op':a_op,
                'vw':vw,
                'aw':aw,
                'result':re,
                'redict':redict,
                'ctype':ctype,
                'ttype':ttype,
                'vtype':vtype
                }
                return render(request,'calc/wattstoamps.html',context)
            elif ctype == 'form3' and ttype == 'form3' and pf and a and p and vtype:
                ctype = request.POST['ctype']
                vtype = request.POST['vtype']
                a = float(request.POST['a'])
                pf = float(request.POST['pf'])
                p = float(request.POST['p'])
                a_op = request.POST['a_op']
                p_op = request.POST['p_op']

                aw = ampereconverter(a_op,a)
                pw = wattconverter(p_op,p)

                if vtype == 'form1':
                    re =  pw / (math.sqrt(3) * pf * aw)
                    formula = "P / (√3 * PF * I)"
                    f = True
                else:
                    re = pw / (3 * pf * aw)
                    formula = "P / (3 * PF * I)"
                    f = False
                
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Watts (W)':re,'MilliWatts (mW)':re * 1000,'MegaWatts (MW)': re/1000000,'KiloWatts (kW)':re/1000,'GigaWatts (GW)':re/1000000000,'British Thermal Unit per hour (BTU/h)':re*3.412141633,'Electric horse Power (hp(E))':re/746}
                context = {
                'f':f,
                'formula':formula,
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'a':a,
                'pf':pf,
                'p':p,
                'p_op':p_op,
                'a_op':a_op,
                'pw':pw,
                'aw':aw,
                'result':re,
                'redict':redict,
                'ctype':ctype,
                'ttype':ttype,
                'vtype':vtype
                }
                return render(request,'calc/wattstoamps.html',context)
            elif ctype == 'form3' and ttype == 'form4' and v and a and p and vtype:
                ctype = request.POST['ctype']
                vtype = request.POST['vtype']
                a = float(request.POST['a'])
                v = float(request.POST['v'])
                p = float(request.POST['p'])
                a_op = request.POST['a_op']
                p_op = request.POST['p_op']
                v_op = request.POST['v_op']


                aw = ampereconverter(a_op,a)
                pw = wattconverter(p_op,p)
                vw = voltconverter(v_op,v)

                if vtype == 'form1':
                    re =  pw / (math.sqrt(3) * vw * aw)
                    formula = "P / (√3 * V * I)"
                    f = True
                else:
                    re = pw / (3 * vw * aw)
                    formula = "P / (3 * V * I)"
                    f = False
                if re >= 1 or re <=0:
                    messages.error(request,'Power factor should be in the range from 0 to 1')
        
                
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    r11 = str(re)
                    index_num = r11.index('e')
                    stratpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                'f':f,
                'formula':formula,
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'a':a,
                'v':v,
                'p':p,
                'p_op':p_op,
                'a_op':a_op,
                'v_op':v_op,
                'vw':vw,
                'pw':pw,
                'aw':aw,
                'result':re,
                'ctype':ctype,
                'ttype':ttype,
                'vtype':vtype
                }
                return render(request,'calc/wattstoamps.html',context)


            return render(request,'calc/wattstoamps.html',{'ctype':ctype,'ttype':ttype,'vtype':vtype})
        else:
            return render(request,'calc/wattstoamps.html',{'ctype':ctype,'ttype':ttype,'vtype':vtype})
    except:
        messages.error(request,"Please enter valid data")
        return render(request,'calc/wattstoamps.html',{'ctype':ctype,'ttype':ttype,'vtype':vtype})