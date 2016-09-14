#!/bin/bash -xe

find ./hyph-utf8-belarusian -name \*-be.\* -delete
cp ./hyph-be.tex ./hyph-utf8-belarusian/tex/generic/hyph-utf8/patterns/tex/

pushd ./hyph-utf8-belarusian/source/generic/hyph-utf8/

./generate-pattern-loaders.rb
./generate-plain-patterns.rb
./generate-ptex-patterns.rb

popd
pushd ./hyph-utf8-belarusian

mkdir -p ../texlive-hyph-belarusian_2014.20141024-1_all/usr/share/texlive/texmf-dist/tex/generic/hyph-utf8/patterns/txt/
mkdir -p ../texlive-hyph-belarusian_2014.20141024-1_all/usr/share/texlive/texmf-dist/tex/generic/hyph-utf8/patterns/tex/
mkdir -p ../texlive-hyph-belarusian_2014.20141024-1_all/usr/share/texlive/texmf-dist/tex/generic/hyph-utf8/patterns/ptex/
mkdir -p ../texlive-hyph-belarusian_2014.20141024-1_all/usr/share/texlive/texmf-dist/tex/generic/hyph-utf8/patterns/quote/
mkdir -p ../texlive-hyph-belarusian_2014.20141024-1_all/usr/share/texlive/texmf-dist/tex/generic/hyph-utf8/loadhyph/

find . -name '*-be.*' -exec install -m 644 -T '{}' ../texlive-hyph-belarusian_2014.20141024-1_all/usr/share/texlive/texmf-dist/'{}' \;

popd

fakeroot dpkg-deb -b ./texlive-hyph-belarusian_2014.20141024-1_all/
