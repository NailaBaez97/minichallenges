#include <iostream>
#include <string>
#include <limits>
using namespace std;

int main()
{
    string cadena_original;
    cout << "Ingrese una cadena de caracteres: ";
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Limpiar el buffer de entrada
    getline(cin, cadena_original);                       // Leer toda la línea incluyendo espacios

    string cadena_invertida = "";
    for (int i = cadena_original.length() - 1; i >= 0; i--)
    {
        cadena_invertida += cadena_original[i];
    }

    if (cadena_original == cadena_invertida)
    {
        cout << "La cadena es un palíndromo." << endl;
    }
    else
    {
        cout << "La cadena no es un palíndromo." << endl;
    }
    return 0;
}
