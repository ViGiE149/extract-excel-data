function handleFileSelect(input) {
    if (input.files && input.files.length > 0) {
        input.classList.add('green-input');
    } else {
        input.classList.remove('green-input');
    }
}

