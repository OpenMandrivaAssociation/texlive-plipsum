# revision 27670
# category Package
# catalog-ctan /macros/plain/contrib/plipsum
# catalog-date 2012-09-14 20:13:55 +0200
# catalog-license lppl
# catalog-version 2.3
Name:		texlive-plipsum
Version:	2.3
Release:	1
Summary:	'Lorem ipsum' for Plain TeX developers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/plipsum
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plipsum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plipsum.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a paragraph generator designed for use in
Plain TeX documents. The paragraphs generated contain many 'f-
groups' (ff, fl etc.) so the text can act as a test of the
ligatures of the font in use.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/plipsum/plipsum.tex
%doc %{_texmfdistdir}/doc/plain/plipsum/README
%doc %{_texmfdistdir}/doc/plain/plipsum/compile.sh
%doc %{_texmfdistdir}/doc/plain/plipsum/plipsum.nw
%doc %{_texmfdistdir}/doc/plain/plipsum/plipsumdoc.pdf
%doc %{_texmfdistdir}/doc/plain/plipsum/pliptest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
