Shared Dependencies:

1. Exported Variables:
   - DENSITIES: A dictionary containing the density values for the filaments. It is used in the backend to calculate the weight of the 3D model.

2. Data Schemas:
   - PrintEstimate: A class in the backend that calculates the weight, cost, sale price, and gross profit margin of the 3D model. It is used in the estimator.py and estimator_router.py files.
   - FileUpload: A FastAPI data schema used in the upload_router.py file to handle file uploads.

3. ID Names of DOM Elements:
   - upload-file-input: The input field for file uploads in the UploadForm.astro component.
   - filament-selector: The select field for filament type in the FilamentSelector.astro component.
   - infill-selector: The select field for infill percentage in the InfillSelector.astro component.
   - submit-button: The button for submitting the form in the SubmitButton.astro component.
   - model-preview: The section for displaying the 3D model preview in the ModelPreview.astro component.
   - price-estimate: The section for displaying the price estimate in the PriceEstimate.astro component.

4. Message Names:
   - uploadFile: A function in the api.js file that sends a POST request to the backend to upload a file.
   - getEstimate: A function in the api.js file that sends a GET request to the backend to get the price estimate.

5. Function Names:
   - calculate_weight: A function in the PrintEstimator class that calculates the weight of the 3D model.
   - calculate_pricing: A function in the PrintEstimator class that calculates the cost, sale price, and gross profit margin.
   - estimate: A function in the PrintEstimator class that estimates the weight, dimensions, cost, sale price, and gross profit margin.
   - handleFileUpload: A function in the UploadForm.astro component that handles file uploads.
   - handleFilamentChange: A function in the FilamentSelector.astro component that handles changes in the filament type.
   - handleInfillChange: A function in the InfillSelector.astro component that handles changes in the infill percentage.
   - handleSubmit: A function in the SubmitButton.astro component that handles form submission.