<html>
<body>
% if defined('error_message'):
<b>Error: {{ error_message }}</b>
% end
<form action="/" method="post" enctype="multipart/form-data">
  Repeat times:      <input type="text" name="repeat_number" />
  Select a file: <input type="file" name="upload_file" />
  <input type="submit" value="Upload" />
</form>
</body>
</html>
