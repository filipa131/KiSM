#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

string affine_decrypt(const string& str, int a, int b) {
    string decrypted = "";
    for (char c : str) {
        if (isalpha(c)) {
            bool is_upper = isupper(c);
            c = tolower(c);
            int char_index = c - 'a';
            int decrypted_index = (a * char_index - b + 26) % 26;
            char decrypted_char = decrypted_index + 'a';
            if (is_upper) {
                decrypted_char = toupper(decrypted_char);
            }
            decrypted += decrypted_char;
        } else {
            decrypted += c;
        }
    }
    return decrypted;
}

int main() {   
    string str;
    cout << "Input text: ";
    cin >> str;

    for (int a = 0; a <= 26; a++){
        for (int b = 0; b <= 26; b++){
            string decrypted_text = affine_decrypt(str, a, b);
            cout << "f(x) = " << a << "x + " << b << endl;
            cout << "Decrypted text: " << decrypted_text << endl;
            cout << "------------------------" << endl;
        }
    }
    
    return 0;
}
