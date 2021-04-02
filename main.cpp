// This is a program intended for aiding in the creation of audio.
// Written by Holden Green (holdengreen.org) for the Green Empower organization (greenempower.org).

#include <iostream>
#include <fstream>
#include <ios>

using namespace std;

struct RIFF_HEADER
{
	char szRiffID[4]; // "RIFF"
	uint64_t dwRiffSize;
	char szRiffFormat[4]; // "WAVE"
};

struct WAVE_FORMAT
{
	uint32_t wFormatTag;
	uint32_t wChannels;
	uint64_t dwSamplesPerSec;
	uint64_t dwAvgBytesPerSec;
	uint32_t wBlockAlign;
	uint32_t wBitsPerSample;
};

struct FMT_BLOCK
{
	char szFmtID[4]; // "fmt "
	uint64_t dwFmtSize;
	WAVE_FORMAT wavFormat;
};

struct DATA_BLOCK
{
	char szDataID[4]; // "data"
	uint64_t dwDataSize;
};

struct NOTE_CHUNK
{
	char ID[4]; // "note"
	long chunkSize;
	long dwIdentifier;
	char dwText[];
};

int main ( ) {
	cout << "Hello Audio Lab!" << endl;

	fstream fl("output.wav", ios::binary);

	return 0;
}
