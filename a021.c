#include <stdio.h>
#include <string.h>

int main(void) {
    // Input
    char s1[500], op, s2[500];
    scanf("%s %c %s", s1, &op, s2);

    // Convert char array to INVERTED int array
    int d1[500], d2[500], d[1000], i, j, k, m, n, True, result, carry = 0, sign;
    for(i = 0; i < 500; i++)
        d1[i] = 0, d2[i] = 0;
    for(i = 0; i < 1000; i++)
        d[i] = 0;
    for(i = 0, j = strlen(s1) - 1; j >= 0; i++, j--)
        d1[i] = s1[j] - '0';
    for(i = 0, j = strlen(s2) - 1; j >= 0; i++, j--)
        d2[i] = s2[j] - '0';

    // Execute one arithmetic op out of 4
    if(op == '+'){
        for(i = 0; i < 500; i++){
            result = carry + d1[i] + d2[i];
            carry = result / 10;
            d[i] = result % 10;}}

    if(op == '-'){
        for(i = 499; i >= 0; i--){
            if(d1[i] > d2[i]){
                sign = 1;
                break;}
            if(d1[i] < d2[i]){
                sign = -1;
                break;}}
        for(i = 0; i < 500; i++){
            result = carry + (d1[i] - d2[i]) * sign + 10;
            carry = result / 10 - 1;
            d[i] = result % 10;}}

    if(op == '*'){
        for(i = 0; i < 500; i++){
            for(j = 0; j < 500; j++){
                result = carry + d1[i] * d2[j] + d[i+j];
                carry = result / 10;
                d[i+j] = result % 10;}}}

    if(op == '/'){
        int lens1 = strlen(s1);
        int lens2 = strlen(s2);
        for(k = lens2 - 1; k < lens1; k++){
            while(k >= lens2 && s1[k-lens2] != '0'){
                for(i = k, j = lens2 - 1; j >= 0; i--, j--){
                    result = carry + s1[i] - s2[j] + 10;
                    carry = result / 10 - 1;
                    s1[i] = result % 10 + '0';}
                s1[i] += carry;
                carry = 0;
                d[k] += 1;}
            do{
                for(m = k - lens2 + 1, n = 0; n < lens2; m++, n++){
                    True = 0;
                    if(s1[m] > s2[n]){
                        True = 1001000;
                        for(i = k, j = lens2 - 1; j >= 0; i--, j--){
                            result = carry + s1[i] - s2[j] + 10;
                            carry = result / 10 - 1;
                            s1[i] = result % 10 + '0';}
                        d[k] += 1;
                        break;}
                    if(s1[m] < s2[n])
                        break;
                    if(n == lens2 - 1){
                        d[k] += 1;
                        for(i = k, j = lens2 - 1; j >= 0; i--, j--)
                            s1[i] = '0';}}}while(True);
            if(!(k == lens2 -1 && d[k] == 0))
                printf("%d", d[k]);}}

    // INVERT INVERTED int array
    for(i = 499; i >= 0; i--){
        if(d[i] != 0)
            break;
        if(i == 0){
            printf("0");
            return 0;}}

    // Output of +, -, *
    if(op != '/'){
        if(sign == -1)
            printf("-");
        for(; i >= 0; i--)
            printf("%d", d[i]);}

    return 0;
}
