export function validateFile(file) {
    const validFileTypes = ['3mf', 'stl'];
    const extension = file.name.split('.').pop().toLowerCase();
    return validFileTypes.includes(extension);
}

export function getFileSize(file) {
    const sizeInBytes = file.size;
    const sizeInKilobytes = sizeInBytes / 1024;
    const sizeInMegabytes = sizeInKilobytes / 1024;
    return sizeInMegabytes.toFixed(2);
}