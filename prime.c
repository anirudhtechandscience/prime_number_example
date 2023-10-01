#include <stdio.h>
#include <stdbool.h>

// i would have used pointers and header files, but that adds complexity for beginners so i chose not to
bool check(int prime){
	bool is_prime;
	int cnt = 0;
	if (prime == 1 || prime == 2){ // doesnt work for if it is one, two isnt neccsary but i added it anyways
		is_prime = true;
	} else {
		for (int i = 1; i <= prime; i++){
			int mod = prime % i;// use mod to calculate remainder,then check if divisible
			if (mod == 0){ //checks for divisibility
				cnt++;
			} else {
				mod = 0;//just a reset
			}
	}
	if (cnt == 2){// prime number is divisble by itself and one, which is why it doesnt work for one
		is_prime = true;
	} else {
		is_prime = false;
	}
	return is_prime;
}
}

int main(void){
	int input;
	printf("Please enter which number you want to check is prime\n");
	scanf("%i", &input);
		bool result = check(input);
		printf("%i is prime : %d\n", input , result);
		return 0;
}



