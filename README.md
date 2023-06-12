# PixelPushupAPI Documentation

![Image Alt Text](images/pushup.webp)

The PixelPushupAPI is a Flask-based API that allows users to upload images, resize them, and store the resized versions in an S3 bucket. This documentation provides an overview of the API endpoints, request/response formats, and important considerations.

## Endpoints

### Test Endpoint

- **Endpoint**: `/`
- **HTTP Method**: GET
- **Description**: A test endpoint to check if the API is up and running.
- **Response**: A plain text message indicating the API status.

### Image Pushup

- **Endpoint**: `/pushup`
- **HTTP Method**: POST
- **Description**: Uploads an image and generates resized versions of the image.
- **Request**:

  - Form Data:
    - `image`: The image file to be uploaded (multipart/form-data).

- **Response**:
  - HTTP Status: 200 OK
  - Body: JSON object containing the following information:
    - `message`: A success message indicating that the image was processed and uploaded successfully.
    - `original`: Details of the original image:
      - `filename`: The filename of the original image.
      - `size`: The dimensions of the original image.
      - `file_size`: The file size of the original image.
      - `file_type`: The MIME type of the original image.
    - `images`: An array of resized image details, each containing:
      - `filename`: The filename of the resized image.
      - `size_name`: The size name of the resized image (t, s, m, l).
      - `size`: The dimensions of the resized image.
      - `file_size`: The file size of the resized image.
      - `url`: The URL of the resized image stored in the S3 bucket.

## Response Codes

- **200 OK**: The request was successful, and the response contains the expected data.
- **400 Bad Request**: The request was malformed or missing required parameters.
- **500 Internal Server Error**: An error occurred on the server-side.

## Usage

To use the PixelPushupAPI, you can send an HTTP POST request to the `/pushup` endpoint, including the image file as form data. The API will process the image, generate resized versions, and store them in an S3 bucket. The response will contain information about the original image and the URLs of the resized images.

## Requirements

- Python 3.10
- Flask
- Pillow (PIL)
- boto3
- flask-cors

## Deployment

The PixelPushupAPI can be deployed as a Lambda function using Zappa. Zappa allows you to package and deploy Flask applications as serverless functions on AWS Lambda. The `zappa_settings.json` file contains the configuration settings for the Zappa deployment.

1. Ensure you have the necessary AWS credentials set up.
2. Install the required Python dependencies: `pip install flask flask-cors pillow boto3 zappa`.
3. Set `S3_BUCKET_NAME` in your environment variables.
4. Run the application locally for testing: `python main.py`.
5. Configure your AWS credentials using the AWS CLI: `aws configure`.
6. Deploy the application to AWS Lambda using Zappa: `zappa deploy dev`.

## Conclusion

The PixelPushupAPI provides a simple and efficient way to upload images, generate resized versions, and store them in an S3 bucket. By leveraging Flask, AWS Lambda, and S3, you can easily integrate image uploading and resizing functionality into your applications.

## Example output.

```json
{
  "images": [
    {
      "file_size": "8.94 KB",
      "filename": "mainstream-hotel",
      "size": [100, 61],
      "size_name": "t",
      "url": "https://pixelpushup-test.s3.amazonaws.com/t/mainstream-hotel.webp"
    },
    {
      "file_size": "61.68 KB",
      "filename": "mainstream-hotel",
      "size": [300, 183],
      "size_name": "s",
      "url": "https://pixelpushup-test.s3.amazonaws.com/s/mainstream-hotel.webp"
    },
    {
      "file_size": "147.91 KB",
      "filename": "mainstream-hotel",
      "size": [500, 305],
      "size_name": "m",
      "url": "https://pixelpushup-test.s3.amazonaws.com/m/mainstream-hotel.webp"
    },
    {
      "file_size": "331.43 KB",
      "filename": "mainstream-hotel",
      "size": [800, 487],
      "size_name": "l",
      "url": "https://pixelpushup-test.s3.amazonaws.com/l/mainstream-hotel.webp"
    },
    {
      "file_size": "483.72 KB",
      "filename": "mainstream-hotel",
      "size": [1000, 609],
      "size_name": "xl",
      "url": "https://pixelpushup-test.s3.amazonaws.com/xl/mainstream-hotel.webp"
    },
    {
      "file_size": "609.99 KB",
      "filename": "mainstream-hotel",
      "size": [1141, 695],
      "size_name": "xxl",
      "url": "https://pixelpushup-test.s3.amazonaws.com/xxl/mainstream-hotel.webp"
    }
  ],
  "message": "Image processed and uploaded successfully.",
  "original": {
    "file_size": "1.09 MB",
    "file_type": "image/png",
    "filename": "mainstream-hotel",
    "size": [1141, 695]
  }
}
```
