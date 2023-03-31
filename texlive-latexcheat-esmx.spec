Name:		texlive-latexcheat-esmx
Version:	36866
Release:	2
Summary:	A LaTeX cheat sheet, in Spanish
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latexcheat/latexcheat-esmx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-esmx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-esmx.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
