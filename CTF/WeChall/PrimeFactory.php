<?php 

$i = 2;
$flag0 = 0;
$flag1 = 0;
$array = array();

while ($i<100 && $flag==0) {

	for ($j=2; $j<$i; $j++ ) {
	
		if ($i%$j!=0) { 
			
			for ($k=0; $k<count($array); $k++) {
			
				$x = $i%10;
				$y = (int) ($i/10);
				$array[$k] = $x;

			
			}
			
			$sum = 0;

			for ($k=0; $k<count($array); $k++) { 

				$sum = $sum + $array[$k];
			}

			primeNumbers($sum);


	}

	$i++;

	}

}
/*
$x = (int) 12345%10;
$y = (int) (12345/10);
$z = 12345%1000; 

echo "x -> " . $x . "<br>";
echo "y -> " . $y . "<br>";
echo "z -> " . $z . "<br>";

*/
function primeNumbers($t){

	$x = $t;
	$flag = 0;

 	for ($a=2 ; $a<$x; $a++) {

 		$z = 0;

 		for($i=2 ; $i<$a ; $i++){

 			if($a%$i == 0){

 				$flag = 1;
 				break;
 			
 			}
 		
 		}

 		// if($z==0) echo $a . '<br>';
 		
 		if($z==0){
 			echo $X;
 		}
 	}