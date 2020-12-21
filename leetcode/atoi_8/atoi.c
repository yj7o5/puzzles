#include <stdio.h>
#include <stdint.h>


int atoi_solution(char* s) {

    int32_t result = 0;
    int8_t sign = 1;
    uint8_t i = 0;

    // discard whitespaces in the beginning
    while (s[i] != '\0' && s[i] == ' ')
        i++;

    // check if optional sign exists
    if (s[i] == '-' || s[i] == '+')
        sign = s[i++] == '-' ? -1 : 1;

    while (s[i] != '\0' && (s[i] >= '0' && (s[i]) <= '9')) {
        if (
            result > INT32_MAX/10 || 
            (result == INT32_MAX/10 && s[i]-'0' > INT32_MAX%10))
        {
            return sign == 1 ? INT32_MAX : INT32_MIN;
        }

        result = result*10 + (s[i++] - '0');
    } 

    return sign*result;
}


int my_atoi(char* s) {
    int32_t result = 0;
    int8_t sign = 1;
    uint8_t i = 0;

    // discard whitespaces in the beginning
    while (s[i] != '\0' && s[i] == ' ')
        i++;

    // check if optional sign exists
    if (s[i] == '-' || s[i] == '+')
        sign = s[i++] == '-' ? -1 : 1;

    int8_t pop = 0;
    while (s[i] != '\0' && (s[i] >= '0' && (s[i]) <= '9')) {
        pop = sign * (s[i] - 48);
        
        /* DEBUG
        const char* template = "pop: %i s[i]: %c s[i](dec): %i result: %d\n";
        printf(template, pop, s[i], (uint8_t)s[i], result);
        */

        if (result > INT32_MAX/10 || (result == INT32_MAX/10 && pop > 7)) {
            return INT32_MAX;
        } 

        if (result < INT32_MIN/10 || (result == INT32_MIN/10 && pop < -8)) {
            return INT32_MIN;
        }

        result = result*10 + pop;
        i += 1;
    } 

    return result;
}

int main(int argc, char* argv[]) {
    printf("42=%d\n", atoi_solution("42"));
    printf("    -42=%d\n", atoi_solution("    -42"));
    printf("4193 with words=%d\n", atoi_solution("4193 with words"));
    printf("words and 987=%d\n", atoi_solution("words and 987"));
    printf("-91283472332=%d\n", atoi_solution("-91283472332"));
    printf("-+12=%d\n", atoi_solution("-+12"));
    printf("=%d\n", atoi_solution(""));
    printf("  =%d\n", atoi_solution("  "));
    printf("2147483647=%d\n", atoi_solution("2147483647"));
    printf("2147483648=%d\n", atoi_solution("2147483648"));
    printf("-2147483648=%d\n", atoi_solution("-2147483648"));
    printf("-2147483649=%d\n", atoi_solution("-2147483649"));

    return 0;  
}
