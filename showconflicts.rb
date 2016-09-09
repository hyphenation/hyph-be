#!/usr/bin/env ruby

require './hydra/lib/hydra'
hydra = Hydra.new
hydra.ingest_file './hyph-be.tex'
puts hydra.conflicts
