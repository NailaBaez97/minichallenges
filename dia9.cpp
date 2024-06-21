// Escribir un programa que pida al usuario dos números y los sume. ¡Pero esta vez hazlo en C++! :)
#include <iostream>

using namespace std;

int main()
{
    int numero1;
    int numero2;
    int suma;

    cout << ("Ingrese el primer  numero:") << endl;
    cin >> numero1;

    cout << ("Ingrese el segundo numero:") << endl;
    cin >> numero2;

    suma = numero1 + numero2;

    cout << ("La suma de los numeros es: ") << suma;

    return 0;
}
