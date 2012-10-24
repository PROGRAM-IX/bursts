#! /bin/bash

sox -n note_c.$1 synth .05 $2 523
sox -n note_d.$1 synth .05 $2 587
sox -n note_e.$1 synth .05 $2 659
sox -n note_f.$1 synth .05 $2 698
sox -n note_g.$1 synth .05 $2 784
sox -n note_a.$1 synth .05 $2 880
sox -n note_b.$1 synth .05 $2 987
sox -n note_hc.$1 synth .05 $2 1046
