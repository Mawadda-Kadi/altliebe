console.log("START")

// document.getElementById('{{ form.image.id_for_label }}').addEventListener('change', function (event) {
//     if (event.target.files.length > 0) {
//         var src = URL.createObjectURL(event.target.files[0]);
//         var preview = document.getElementById('img_preview_{{ forloop.counter0 }}');
//         preview.src = src;
//         preview.style.display = 'block';
//     }
// });

function readURL(input, previewId) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            var previewImage = document.querySelector(previewId);
            if (previewImage) {
                previewImage.src = e.target.result;
            }
        }
        reader.readAsDataURL(input.files[0]);
    }
}

// Main image preview
document.addEventListener('DOMContentLoaded', function () {
    var featuredImageInput = document.getElementById('id_featured_image');
    featuredImageInput.addEventListener('change', function () {
        readURL(this, '#featured_image_preview img');
    });

    // Additional images preview
    var additionalImagesInputs = document.querySelectorAll("#additional_images_preview input[type='file']");
    additionalImagesInputs.forEach(function (input, index) {
        input.addEventListener('change', function () {
            readURL(this, '#img_preview_' + index);
        });
    });
});

// function readURL(input, previewId) {
//     if (input.files && input.files[0]) {
//         var reader = new FileReader();
//         reader.onload = function (e) {
//             $(previewId).attr('src', e.target.result);
//         }
//         reader.readAsDataURL(input.files[0]);
//     }
// }

// $(document).ready(function () {
//     // Main image preview
//     $("#id_featured_image").change(function () {
//         readURL(this, '#featured_image_preview img');
//     });


//     // Additional images preview
//     $("#additional_images_preview input[type='file']").each(function (index) {
//         $(this).change(function () {
//             readURL(this, '#additional_images_preview .image-preview img:eq(' + index + ')');
//         });
//     });
// });

