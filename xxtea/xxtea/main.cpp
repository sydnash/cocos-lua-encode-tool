#include "xxtea.h"
#include "string.h"
#include "stdlib.h"
#include <fstream>

using namespace std;
int main(int argc, char **argv)
{
	//exe infile outfile key sign de[en]
	if (argc < 5) {
		printf("param is not ok");
		return 0;
	}
	auto infile = argv[1];
	auto outfile = argv[2];
	char *key = argv[3];
	char *sign = argv[4];
	bool en = true;
	if (argc >= 6) {
		auto ten = argv[5];
		if (strcmp(ten, "en") == 0) {
			en = true;
		}
		else {
			false;
		}
	}

	int key_len = strlen(key);
	int sign_len = strlen(sign);

	fstream input(infile, std::fstream::in | std::fstream::binary);
	input.seekg(0, input.end);
	int length = input.tellg();
	input.seekg(0, input.beg);

	unsigned char * buffer = new unsigned char[length + 1];
	input.read((char*)buffer, length);
	input.close();

	if (length <= 0) {
		printf("%s open failed", infile);
		return 0;
	}
	unsigned char* ret = nullptr;
	size_t retlen = 0;
	if (en) {
		ret = xxtea_encrypt(buffer, length, (unsigned char*)key, key_len, &retlen);
	} else {
		ret = xxtea_decrypt(buffer + sign_len, length - sign_len, (unsigned char*)key, key_len, &retlen);
	}

	fstream output(outfile, std::fstream::out | std::fstream::binary);
	if (en) {
		output.write(sign, sign_len);
	}
	output.write((char*)ret, retlen);
	output.close();

	free(ret);
	return 0;
}