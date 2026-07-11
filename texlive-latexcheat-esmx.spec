%global tl_name latexcheat-esmx
%global tl_revision 36866

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.00
Release:	%{tl_revision}.1
Summary:	A LaTeX cheat sheet, in Spanish
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latexcheat/latexcheat-esmx
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-esmx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-esmx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a translation to Spanish (Castellano) of Winston Chang's LaTeX
cheat sheet (a reference sheet for writing scientific papers).

