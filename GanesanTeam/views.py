from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from GanesanTeam.models import Login, ClaimType, RequestFrom, Region, Category, SubCategory, Claimsstatus, \
    AdditionalClaimsstatus, Originator, Tracker
import logging
logger = logging.getLogger('django')

# Create your views here.

def home(request):
    if 'username' in request.session:
        ClaimTypes = ClaimType.objects.all()
        RequestFroms = RequestFrom.objects.all()
        Regions = Region.objects.all()
        Categories = Category.objects.all()
        SubCategories = SubCategory.objects.all()
        Claimsstatuss = Claimsstatus.objects.all()
        AdditionalClaimsstatuss = AdditionalClaimsstatus.objects.all()
        Originators = Originator.objects.all()
        Context = {'username': request.session['username'], 'claimtypes': ClaimTypes, 'requestfroms': RequestFroms,
                   'regions': Regions, 'categories': Categories, 'subcategories': SubCategories,
                   'claimsstatuss': Claimsstatuss, 'additionalclaimsstatuss': AdditionalClaimsstatuss,
                   'originators': Originators}
        return render(request, 'index.html', context=Context)
    else:
        usernames = Login.objects.all()
        context = {'usernames': usernames}
        return render(request, 'login.html', context=context)


def login(request):
    usernames = Login.objects.all()
    context = {'usernames': usernames}
    return render(request, 'login.html', context=context)

def logout(request):
    del request.session['username']
    usernames = Login.objects.all()
    context = {'usernames': usernames}
    return render(request, 'login.html',context=context)

def processlogin(request):
    email = request.POST["Email"]
    request.session['email'] = email
    password = request.POST["Password"]
    login_query = Login.objects.all()
    loginbool = False

    logger.info(str(email) + str(" loggedin ") + str(datetime.now()))

    for login in login_query:
        if str(login.username).upper() == str(email).upper() and str(login.password).upper() == str(password).upper():
            loginbool = True

    if loginbool == True:
        request.session['username'] = str(email).split("@")[0].split(".")[0]
        ClaimTypes = ClaimType.objects.all()
        RequestFroms = RequestFrom.objects.all()
        Regions = Region.objects.all()
        Categories = Category.objects.all()
        SubCategories = SubCategory.objects.all()
        Claimsstatuss = Claimsstatus.objects.all()
        AdditionalClaimsstatuss = AdditionalClaimsstatus.objects.all()
        Originators = Originator.objects.all()
        Context = {'username': request.session['username'], 'claimtypes': ClaimTypes, 'requestfroms': RequestFroms,
                   'regions': Regions, 'categories': Categories, 'subcategories': SubCategories,
                   'claimsstatuss': Claimsstatuss, 'additionalclaimsstatuss': AdditionalClaimsstatuss,
                   'originators': Originators}
        return render(request, 'index.html', context=Context)
    else:
        usernames = Login.objects.all()
        context = {'usernames': usernames}
        return render(request, 'login.html', context=context)


def claimformsubmit(request):

    if 'username' in request.session:
        try:
            claimtype = request.POST.get("claimtype")
            claim_ref = request.POST.get("claimref")
            request_from = request.POST.get("requestfrom")

            if request.POST.get("requestdate"):
                req_date = datetime.strptime(request.POST.get("requestdate"), "%d-%m-%Y").date()
            else:
                req_date =None

            if request.POST.get("currentdate"):
                current_date = datetime.strptime(request.POST.get("currentdate"), "%d-%m-%Y").date()
            else:
                current_date =None


            region = request.POST.get("region")
            category = request.POST.get("category")
            subcategory = request.POST.get("subcategory")

            if request.POST.get("claimeddate"):
                claim_date = datetime.strptime(request.POST.get("claimeddate"), "%d-%m-%Y").date()
            else:
                claim_date =None

            customer = request.POST.get("customer")
            purchase_order = request.POST.get("purchaseorder")
            cbn = request.POST.get("cbn")
            hporder = request.POST.get("hporder")
            recieved_partno = request.POST.get("recievedpartno")
            claimed_partno = request.POST.get("claimedpartno")
            qty = request.POST.get("qty")
            packid = request.POST.get("packid")
            boxid = request.POST.get("boxid")
            serialno = request.POST.get("serialno")
            unitprice = request.POST.get("unitprice")
            totalamount = request.POST.get("totalamount")
            hpinvno = request.POST.get("hpinvno")
            redingtoninvoice = request.POST.get("redingtoninvoice")

            if request.POST.get("ecidate"):
                ecidate = datetime.strptime(request.POST.get("ecidate"), "%d-%m-%Y").date()
            else:
                ecidate = None

            if request.POST.get("calliddate"):
                calliddate = datetime.strptime(request.POST.get("calliddate"), "%d-%m-%Y").date()
            else:
                calliddate =None


            rrno = request.POST.get("rrno")
            customercm = request.POST.get("customercm")
            dhlcode = request.POST.get("dhlcode")
            rponum = request.POST.get("rponum")

            if request.POST.get("rpodate"):
                rpodate = datetime.strptime(request.POST.get("rpodate"), "%d-%m-%Y").date()
            else:
                rpodate =None

            if request.POST.get("grndate"):
                grndate = datetime.strptime(request.POST.get("grndate"), "%d-%m-%Y").date()
            else:
                grndate =None


            hpcnno = request.POST.get("hpcnno")

            if request.POST.get("hpcndate"):
                hpcndate = datetime.strptime(request.POST.get("hpcndate"), "%d-%m-%Y").date()
            else:
                hpcndate =None

            hpcnvalue = request.POST.get("hpcnvalue")
            ca_ca = request.POST.get("ca=ca")
            aging = request.POST.get("aging")
            claimstatus = request.POST.get("claimstatus")
            additionalclaims = request.POST.get("additionalclaims")
            originator = request.POST.get("Originator")
            remarks = request.POST.get("remarks")

            tracker = Tracker(
                claimtype=claimtype,
                claim_ref=claim_ref,
                request_from=request_from,
                req_date=req_date,
                current_date=current_date,
                region=region,
                category=category,
                subcategory=subcategory,
                claim_date=claim_date,
                customer=customer,
                purchase_order=purchase_order,
                cbn=cbn,
                hporder=hporder,
                recieved_partno=recieved_partno,
                claimed_partno=claimed_partno,
                qty=qty,
                packid=packid,
                boxid=boxid,
                serialno=serialno,
                unitprice=unitprice,
                totalamount=totalamount,
                hpinvno=hpinvno,
                redington_invoice=redingtoninvoice,
                eci_date=ecidate,
                call_iddate=calliddate,
                rr=rrno,
                customercm_callid=customercm,
                dhlawb_forwardercode =dhlcode,
                rpo=rponum,
                rpo_date=rpodate,
                grn_date=grndate,
                hpcn_no=hpcnno,
                hpcn_date=hpcndate,
                hpcn_value=hpcnvalue,
                ca=ca_ca,
                aging_days=aging,
                claims_status=claimstatus,
                additional_claimsstatus=additionalclaims,
                originator=originator,
                remarks=remarks,
            )
            tracker.save()

            logger.info(str(tracker) + str(" ") + str(datetime.now()))

            return HttpResponse(tracker)

        except Exception as e:

            logger.info(str("Exception occured ") + str(e) + str(" ")+ str(datetime.now()))
            return HttpResponse("Exception occured. " + str(e))


    else:
        usernames = Login.objects.all()
        context = {'usernames': usernames}
        return render(request, 'login.html', context=context)





