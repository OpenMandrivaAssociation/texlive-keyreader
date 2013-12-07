# revision 28195
# category Package
# catalog-ctan /macros/latex/contrib/keyreader
# catalog-date 2012-11-06 20:07:31 +0100
# catalog-license lppl1.3
# catalog-version 0.5b
Name:		texlive-keyreader
Version:	0.5b
Release:	5
Summary:	A robust interface to xkeyval
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keyreader
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyreader.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyreader.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a robust interface to controlling keys in
xkeyval, removing some of that package's restrictions. The
package also addresses some of the issues now covered by the
author's ltxkeys package, which was assumed to be a replacement
for keyreader. Since keyreader has remained a favourite with
users, it has been reinstated.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/keyreader/keyreader.sty
%doc %{_texmfdistdir}/doc/latex/keyreader/README
%doc %{_texmfdistdir}/doc/latex/keyreader/keyreader-example1.tex
%doc %{_texmfdistdir}/doc/latex/keyreader/keyreader-guide.pdf
%doc %{_texmfdistdir}/doc/latex/keyreader/keyreader-guide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
