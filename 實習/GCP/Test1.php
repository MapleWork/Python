<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project</title>

    <link rel="stylesheet" href="Test.css">
    <link rel="stylesheet" href="Test2.php">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/adjx/libs/font-awesome/5.15.4/css/all.min.css">

    <script scr="js/jquery.min.js"></script>
</head>

<body>
    <div class="main-container">
        <div class="aside">
            <div class="nav-toggler">
                <span></span>
            </div>
            <ul class="nav">
                <li><a href="#" class="active"><i class="fa fa-home"></i>人員管理</a></li>
            </ul>
        </div>
        <div class="container">
            <div class="title">人員管理</div>
            <div class="content"> 
                <!-- action="Test2.php" method="POST" -->
                <form  id="form">
                    <div class="user-details">
                        <div class="input-box">
                            <span class="details">Name</span>
                            <input type="text" class="form-control" id="name" name="name" placeholder="Enter your name" required>
                        </div>
                        <div class="input-box">
                            <span class="details">Phone</span>
                            <input type="text" class="form-control" id="phone" name="phone" placeholder="Enter your phone" required>
                        </div>
                        <div class="input-box">
                            <span class="details">Email</span>
                            <input type="text" class="form-control" id="email" name="email" placeholder="Enter your email" required>
                        </div>
                    </div>
                    <div class="button">
                        <!-- <input id="button" type="submit" name="submit" value="新增人員"> -->
                        <button id="button">真正清空</button>
                    </div>
                    <script>
                        $(function(){
                            $("#button").cleck(function(){
                                $("#form :input").not(":button").val("");
                            })
                        })
                    </script>
                    
                </form>
            </div>
        </div>
    </div>
    <?php
        if (isset($_SERVER['HTTP_REFERER'])){
            $THE_REFER=$_SERVER['HTTP_REFERER'];
        }
    ?>
    
</body>
</html>

