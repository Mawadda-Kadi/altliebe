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


