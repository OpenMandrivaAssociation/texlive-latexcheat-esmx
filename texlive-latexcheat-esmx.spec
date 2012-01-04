# revision 16664
# category Package
# catalog-ctan /info/latexcheat/latexcheat-esmx
# catalog-date 2010-01-10 00:40:15 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-latexcheat-esmx
Version:	20100110
Release:	2
Summary:	A LaTeX cheat sheet, in Spanish
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latexcheat/latexcheat-esmx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-esmx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-esmx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a translation to Spanish (Castellano) of Winston
Chang's LaTeX cheat sheet (a reference sheet for writing
scientific papers).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latexcheat-esmx/README
%doc %{_texmfdistdir}/doc/latex/latexcheat-esmx/latexsheet-esmx.pdf
%doc %{_texmfdistdir}/doc/latex/latexcheat-esmx/latexsheet-esmx.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
