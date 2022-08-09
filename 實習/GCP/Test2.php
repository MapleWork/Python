<?php
	$name = $_POST['name'];
	$phone = $_POST['phone'];
	$email = $_POST['email'];

	$DB_NAME = "test";

	// Database connection
	$conn = new mysqli('35.221.182.66','root','test', $DB_NAME);
	if($conn->connect_error){
		echo "$conn->connect_error";
		die("Connection Failed : ". $conn->connect_error);
	} 
	else {
		$stmt = $conn->prepare("insert into test(Name, Phone, Email) values(?, ?, ?)");
		$stmt->bind_param("sss", $name, $phone, $email);
		$execval = $stmt->execute();
	}

	if (empty($conn)) {
		print mysqli_error($conn);
		die("資料庫連接失敗！");
		exit;
	}
	
	// 選取資料庫
	if (!mysqli_select_db($conn, $DB_NAME)) {
		die("選取資料庫失敗！");
	} else {
		
	}
	mysqli_set_charset($conn,"utf8");
	$sql = "SELECT * FROM test";
	$result = mysqli_query($conn, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<title>Project</title>
<head>
	
	<meta charset="utf-8">
	<link rel="stylesheet" href="Test.css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>

<body>
	<div class="container">
		<form action ="Test1.php" method = "POST">
			<button type="submit" name="button">返回上一頁</button>
			<?php
				if(isset($_GET['message'])){
				echo $_GET['message'];
				}
			?>
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
						for($i=1;$i<=mysqli_num_rows($result);$i++){
						$rs=mysqli_fetch_row($result);
						?>
						<tr>
							<td><?php echo $rs[0]?></td>
							<td><?php echo $rs[1]?></td>
							<td><?php echo $rs[2]?></td>

						</tr>
					<?php
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

