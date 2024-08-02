//document.querySelector("#displayYear").innerHTML = currentYear;
// to get current year


//$(function () {
//    $("#claimeddate").datepicker({
//        autoclose: true,
//        todayHighlight: true
//    }).datepicker('update', new Date());
//});


function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();

}

getYear();

// nice select
$(document).ready(function () {
    $('select').niceSelect();
});

// date picker
$(function () {
    $("#customerreqdate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});

$(function () {
    $("#unitcollection").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});

$(function () {
    $("#aspfdr").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#Redinvdate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#ecidatenew").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});

$(function () {
    $("#Duedate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#claimdate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});

$(function () {
    $("#cndate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});



$(function () {
    $("#grndate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#RPODATE").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#RRdate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});



$(function () {
    $("#rpodate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#ecidate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#calliddate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});



$(function () {
    $("#currentdate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});

$(function () {
    $("#requestdate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#ecidate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#calliddate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#grndate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


$(function () {
    $("#hpcndate").datepicker({
        autoclose: true,
        todayHighlight: true
    }).datepicker('update', '');
});


// owl carousel slider js
$('.team_carousel').owlCarousel({
    loop: true,
    margin: 15,
    dots: true,
    autoplay: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1,
            margin: 0
        },
        576: {
            items: 2,
        },
        992: {
            items: 3
        }
    }
})