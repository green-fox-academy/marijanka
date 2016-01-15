<?php
error_reporting(E_ALL & ~E_NOTICE);

session_start();
// session_destroy();

$input = file_get_contents('php://input');
$input_decoded = json_decode($input);



switch ($input_decoded->operation) {
case "edit":
	break;
case "delete":
	foreach ($_SESSION['todos'] as $key=>$row) {
		if ($row['id'] == $input_decoded->id) {
			unset($_SESSION['todos'][$key]);
			break;
		}
	}
	break;
case "list":
	break;
case "update_completed":
	foreach ($_SESSION['todos'] as $key=>$row) {
		if ($row['id'] == $input_decoded->id) {
			$_SESSION['todos'][$key]['completed'] = $input_decoded->completed ? true : false;
			break;
		}
	}
	break;
case "item_save":
	foreach ($_SESSION['todos'] as $key=>$row) {
		if ($row['id'] == $input_decoded->id) {
			$_SESSION['todos'][$key]['subject'] = $input_decoded->subject;
			$_SESSION['todos'][$key]['completed'] = $input_decoded->completed;
			break;
		}
	}
	break;
case "add":
	$_SESSION['todos'][] = array(
		'id' => ++$_SESSION['last_id'],
		'subject' => $input_decoded->subject,
		'completed' => false
	);
	break;
default:
	echo "Hianyzo parameter: muvelet. Ezt kaptuk: " . print_r($input_decoded, true);
}
// Bármilyen műveletet is kérün, mindig visszaadjuk a teljes todo listát.
echo json_encode($_SESSION['todos']);