// This is a program intended for aiding in the creation of audio.
// Written by Holden Green (holdengreen.org) for the Green Empower organization (greenempower.org).

#include <iostream>

#include <vorbis/codec.h>

using namespace std;

int main ( ) {
	cout << "Hello Audio Lab!" << endl;

	void* codec_setup;
	vorbis_dsp_state* dsp_state;
	vorbis_comment* vc;

	ogg_packet *op;
	ogg_packet *op_comm;
	ogg_packet *op_code;

	vorbis_block* vb;

	vorbis_info inf {
		1,
		1,
		1000,

		1000,
		1000,
		1000,
		0, //currently unset

		codec_setup
	};

	vorbis_info_init(&inf);
	vorbis_analysis_init(dsp_state, &inf);
	vorbis_comment_init(vc);
	vorbis_analysis_headerout(dsp_state, vc, op, op_comm, op_code);
	vorbis_block_init(dsp_state, vb);




	return 0;
}
