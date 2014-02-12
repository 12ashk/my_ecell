# /usr/bin/env perl 
# -*- coding: utf-8 -*-

foreach (glob("*.jpg")){
	chomp;
	if(/(\d{2}\.jpg)/){
		rename $_, $&;
	}
}
