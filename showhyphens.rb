#!/usr/bin/env ruby

require './hydra/lib/hydra'
hydra = Hydra.new
hydra.ingest_file './hyph-be.tex'
hydra.setlefthyphenmin 2
hydra.setrighthyphenmin 2

if not ARGV.empty?
  input = ARGV
else
  input = ARGF
end

input.each do |line|
  puts line.split.map{|word| hydra.showhyphens word.strip}.join("\n")
end
