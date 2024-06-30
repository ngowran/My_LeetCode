class Solution {
public:
    std::map<char, int> numbers = {
        {'\0', 0},
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };
    int romanToInt(string s) {
        std::string reversed = "";
        for (int i = s.length() - 1; i >= 0; --i) {
            reversed += s[i];
        }

        char prevChar = '\0';
        int finalNumber = 0;
        for (char character : reversed)
        {
            if (numbers[character] < numbers[prevChar])
            {
                finalNumber -= numbers[character];
            } 
            else
            {
                finalNumber += numbers[character];
            }
            
        prevChar = character;
        }
        return finalNumber;
    }
};
