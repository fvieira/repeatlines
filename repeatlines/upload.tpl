<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <style>
        html {
            margin: 10px;
        }
        .btn-file {
            position: relative;
            overflow: hidden;
        }
        .btn-file input[type=file] {
            display: inline;
        }
        .content {
            width: 450px;
        }
        h1 {
            margin-bottom: 60px;
        }
        .error-message {
            color: red;
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container content">
        <h1>Repeat lines</h1>
        % if defined('error_message'):
            <div class="error-message">Error: {{ error_message }}</div>
        % end
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="repeat_number">Repeat times:</label>
                <input type="text" id="repeat_number" name="repeat_number" />
            </div>
            <div class="form-group">
                <label for="upload_file">Select a file:</label>
                <span class="btn btn-default btn-file">
                    <input type="file" id="upload_file" name="upload_file" />
                </span>
            </div>
            <input type="submit" value="Repeat!" class="btn btn-default" />
        </form>
    </div>
</body>
</html>
