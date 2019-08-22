<!DOCTYPE html>
<html>

<head>
	<link href="fav.ico" rel="icon" type="image/x-icon" />
    <title>Fortuna!</title>
</head>
<center>
	<h1>Temperature & Humidity</h1>
</center>

<?php

$dir_path = "diagram/";
$extensions_array = array('jpg','png','jpeg');

if(is_dir($dir_path))
{
    $files = scandir($dir_path);
    
    for($i = 0; $i < count($files); $i++)
    {
        if($files[$i] !='.' && $files[$i] !='..')
        {
            // get file name
            //echo "File Name -> $files[$i]<br>";
            
            // get file extension
            $file = pathinfo($files[$i]);
            $extension = $file['extension'];
            //echo "File Extension-> $extension<br>";
            
           // check file extension
            if(in_array($extension, $extensions_array))
            {
            // show image
            echo "<img src='$dir_path$files[$i]' style='width:640px;height:480px;'><br>";
            }
        }
    }
}
?>
<body>
</body>
</html>
