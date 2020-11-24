#include <stdio.h>
int R, C, M, x;
int B[10][10];
int A[10][10];
int m[10];

//以下程式碼塊若只有一行則省略{}

//轉置：行列互換
void transpose(){
    for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++)
            A[j][i] = B[i][j];
    x = R;
    R = C;
    C = x;
    for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++)
            B[i][j] = A[i][j];}
//上下翻轉
void flip_upside_down(){
    for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++)
            A[R-1-i][j] = B[i][j];
    for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++)
            B[i][j] = A[i][j];}
//逆時鐘旋轉：先轉置，再上下翻轉
void spin_counterclockwise(){
    transpose();
    flip_upside_down();}

int main() {
    while(scanf("%d%d%d", &R, &C, &M) != EOF){
        for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
				scanf("%d", &B[i][j]);
        
        for(int i = 0; i < M; i++)
			scanf("%d", &m[i]);
        
        for(int k = M-1; k >= 0; k--){
            if(m[k]==0)
                spin_counterclockwise();
            else
                flip_upside_down();}
        
        printf("%d %d\n", R, C);
        for(int i = 0; i < R; i++){
			for(int j = 0; j < C-1; j++)
				printf("%d ", A[i][j]);
            printf("%d\n", A[i][C-1]);}
    }
    return 0;
}
