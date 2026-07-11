%global tl_name plipsum
%global tl_revision 30353

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.3
Release:	%{tl_revision}.1
Summary:	Lorem ipsum for Plain TeX developers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/plipsum
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plipsum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plipsum.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a paragraph generator designed for use in Plain TeX
documents. The paragraphs generated contain many 'f-groups' (ff, fl
etc.) so the text can act as a test of the ligatures of the font in use.

