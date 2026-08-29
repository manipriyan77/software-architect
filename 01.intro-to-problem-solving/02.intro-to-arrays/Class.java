void main() {


//    count the number of elements that are atleast 1 number higher than that number itself
    int[] arr1 = {3, 43, 54, 65, 54, 54, 43,65,77,7,77,77};

    int maxValue = 0;
    int maxCount = 0;
//    for (int j : arr1) {
//        if (j > maxValue) {
//            maxValue = j;
//        }
//    }
//    for (int i : arr1) {
//        if(i==maxValue){
//            maxCount++;
//        }
//    }

    for (int i : arr1) {
        if (i > maxValue) {
            maxValue = i;
            maxCount = 1;
        } else if (i == maxValue) {
            maxCount++;
        }
    }
    System.out.println(arr1.length-maxCount);

}