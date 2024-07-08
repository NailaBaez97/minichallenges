// Ordenamiento de un Array: Escribir un programa que ordene un array de enteros utilizando ¡Pero hazlo en C++! :)
#include <iostream>

using namespace std;

int main()
{
    // Declarar variables y leer datos
    int n;
    cout << ("Ingrese el tamanho del array:  ");
    cin >> n;
    int arr[n];

    for (int i = 0; i < n; i++)
    {
        cout << ("Ingrese el numero entero:  ") << i + 1 << ": ";
        cin >> arr[i];
    }
    // Algoritmo de ordenamiernto por burbuja
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    // imrprimir el array arreglado
    cout << ("Array ordenado:  ");
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
