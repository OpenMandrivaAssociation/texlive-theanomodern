Name:		texlive-theanomodern
Version:	64520
Release:	2
Summary:	Theano Modern fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/theanomodern
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theanomodern.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theanomodern.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the TheanoModern font designed by Alexey
Kryukov, in both TrueType and Type1 formats, with support for
both traditional and modern LaTeX processors. An
artificially-emboldened variant has been provided but there are
no italic variants. The package is named after Theano, a famous
Ancient Greek woman philosopher, who was first a student of
Pythagoras, and supposedly became his wife.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/theanomodern
%{_texmfdistdir}/fonts/vf/public/theanomodern
%{_texmfdistdir}/fonts/type1/public/theanomodern
%{_texmfdistdir}/fonts/truetype/public/theanomodern
%{_texmfdistdir}/fonts/tfm/public/theanomodern
%{_texmfdistdir}/fonts/map/dvips/theanomodern
%{_texmfdistdir}/fonts/enc/dvips/theanomodern
%doc %{_texmfdistdir}/doc/fonts/theanomodern

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
