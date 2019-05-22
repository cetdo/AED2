#include <stdio.h>
#include <stdlib.h>

void QuickSort(int vetor[], int inicio, int fim){
  int i, j, pivo;
  i = inicio; // i recebe o começo do Vetor
  j = fim - 1; // j recebe a posição final do Vetor
  pivo = vetor[(inicio + fim)/2]; //pivo recebe uma posição no meio do vetor

    while(i <= j){ // enquanto a posição inicial for menor ou igual a final

        while(vetor[i] < pivo){ // se o elemento da posição i é menor que o pivo vá para a próxima posição
          i++;
        }

        while (vetor[j] > pivo){ // se o elemento da posição j for maior que o pivo vá para a a próxima posição
          j--;
        }
        // nesse ponto ele deve ter armazenado em i a posição de um elemento maior que o PIVO
        // e em j a posição de um elemento menor que o PIVO
        // case nenhum elemento maior ou menor que o pivo seja encontrado o vetor está ordenado e
        // o valor de i será meior que o valor de J
        if(i <= j){ // se o a posição i for menor ou igual a posição j
          // realiza a troca do valor maior antes do pivo com o valor menor depois do PIVO
          int a = vetor[i];
          vetor[i] = vetor[j];
          vetor[j] = a;
          i ++;
          j --;
        }

        // chama a função recursivamente para a parte anteriror ao PIVO
        if (inicio < j){
          // passa o mesmo vetor como parametro com o inicio marcado como o inicio do Vetor
          // e o final marcado como j que nesse momento é < i e possui o ultimo elemento antes do pivo atual
          QuickSort(vetor, inicio, j);
        }
        // chama a função recursivamente para a parte anterior ao PIVO
        if (i < fim){
        // passa o mesmo vetor como parâmetro com o inicio marcado com i que nesse momento tem a posição posterior a do PIVO
        // e passa como fim a posição final do Vetor
          QuickSort(vetor, i, fim);
        }
    }
}

void printVetor (int vetor[], int tam){
  for (int i = 0; i < tam; i++){
    printf("%i ", vetor[i]);
  }
  printf("\n");
}

int main(){
  int vetor[12], tam = 12;

  for (int i = 0; i < tam; i++){
    vetor[i] = rand() % 100 + 1; // popula o vetor com numeors "aleatórios de 1 a 100"
  }

  printf("Vetor Desordenado: ");
  printVetor(vetor, tam);

  QuickSort(vetor, 0, tam);

  printf("Vetor Ordenado: ");
  printVetor(vetor, tam);
}
