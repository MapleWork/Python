<?php 
include('Test2.php');
if (isset($_POST['action']) && $_POST['action'] == 'submitted') { 
	session_start(); 
	if (isset($_SESSION['submit_time']) && $_SESSION['submit_time']==0){ 
	print '<pre>'; 
	print_r($_POST); 
	print '<a href="'. $_SERVER['PHP_SELF'] .'">Please try again</a>'; 
	print '</pre>'; 
	$_SESSION['submit_time']=1; 
	echo $_SESSION['submit_time']; 
	unset($_SESSION['submit_time']);
	} else { 
	print '<pre>'; 
	print_r($_POST); 
	echo "However you have submitted"; 
	print '</pre>'; 
	} 
	} else { 
	session_start() or dir("session is not started"); 
	$_SESSION['submit_time']= 0; 
	// isset($_SESSION['submit_time']) or die ("session var is not created"); 
	// echo $_SESSION['submit_time']; 
?>
<!DOCTYPE html>
<html lang="en">
<title>Project</title>
<head>
	
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>

<body>

	<?php 
		$query = "SELECT * FROM test"; //搜尋 *(全部欄位) ，從 表staff

		//mysqli_query << PHP 有很多種...指令(?) ，這是其中一個，我現在還都是學到甚麼用什麼，沒辦法自己看手冊，然後實驗+學習使用。 

		$query_run = mysqli_query($name,$phone,$email); //$con <<此變數來自引入的 db_cn.php
	?>
	<div class="container">
		<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST"> 
			<table class="table table-sm table-bordered"style="text-align:center;">
				<thead style="text-align:center;">
					<tr style="text-align:center;">
						<th>Name</th>
						<th>Phone</th>
						<th>Email</th>
					</tr>
				</thead>

				<tbody>
					<!-- 大括號的上、下半部分 分別用 PHP 拆開 ，這樣中間就可以純用HTML語法-->
					<?php
						if(mysqli_num_rows($query_run) > 0)
						{
							foreach($name as $row)
							{
					?>
						<tr>
							<!-- $row['(輸入資料表的欄位名稱)'];  <<用雙引號也行 -->
							<td><?php echo $row['name']; ?></td> 
							<td><?php echo $row['phone']; ?></td> 
							<td><?php echo $row['email']; ?></td>
						</tr>
					<?php
						}
						}
					?>
				</tbody>
		</form>
	</div>
</body>



<!--BOOTSTRAP的東西------------------------------------------------------------------------->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</html>