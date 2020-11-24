#include <stdio.h>
#include <omp.h>
// gcc -Wall measure_omp.c -lgomp

int main(void) {

  float start = 0.0, end = 0.0, elapsed = 0.0;
  start = omp_get_wtime();

  // CUT - Code Under Test

  end = omp_get_wtime();
  elapsed = end-start;
  printf("%f\n", elapsed);


  return 0;
}
