// $(document).ready(function() {
// //SKU 1
// 	$('#form1').on('submit', function(event) {
//
// 		$.ajax({
// 			data : {
// 				outlet : $('#outlet1').val(),
// 				instock : $('#instock1').val(),
// 				onshelf : $('#onshelf1').val()
// 			},
// 			type : 'POST',
// 			url : '/process'
// 		})
// 		.done(function(data) {
//
// 			if (data.error) {
// 				//$('#errorAlert').text(data.error).show();
// 				//$('#successAlert').hide();
//
// 			}
// 			else {
// 				//$('#successAlert').text(data.outlet).show();
// 				//$('#errorAlert').hide();
// 				$('#fade1').fadeTo("slow", 0.10);
// 			}
//
// 		});
//
// 		event.preventDefault();
//
// 	});
// //SKU 5
// 	$('#form5').on('submit', function(event) {
//
// 		$.ajax({
// 			data : {
// 				outlet : $('#outlet5').val(),
// 				instock : $('#instock5').val(),
// 				onshelf : $('#onshelf5').val()
// 			},
// 			type : 'POST',
// 			url : '/process'
// 		})
// 		.done(function(data) {
//
// 			if (data.error) {
// 				//$('#errorAlert').text(data.error).show();
// 				//$('#successAlert').hide();
// 			}
// 			else {
// 				//$('#successAlert').text(data.outlet).show();
// 				//$('#errorAlert').hide();
// 				$('#fade5').fadeTo("slow", 0.10);
// 			}
//
// 		});
//
// 		event.preventDefault();
//
// 	});
//
// });

$(document).ready(function() {
// hide and scroll
        $('.superform').on('submit', function(event) {
                var submitForm = $(this);
                submitForm.find('[type="submit"]').attr('disabled','disabled');
                $.ajax({
                        data : {
                                outlet : submitForm.find('input[name="outletid"]').val(),
								period : submitForm.find('input[name="period"]').val(),
								sku : submitForm.find('input[name="sku"]').val(),
                                instock : submitForm.find('input[name="instock"]:checked').val(),
                                onshelf : submitForm.find('input[name="onshelf"]:checked').val()
                        },
                        type : 'POST',
                        url : '/process'
                })
                .done(function(data) {

                        if (data.error) {
                                //$('#errorAlert').text(data.error).show();
                                //$('#successAlert').hide();

                        }
                        else {
                                //$('#successAlert').text(data.outlet).show();
                                //$('#errorAlert').hide();
                                //$('#fade1').fadeTo("slow", 0.10);
              submitForm.fadeTo("slow",0.1);
              $(document).scrollTop(submitForm.parent().next().offset().top);
                        }

                });

                event.preventDefault();

        });

});