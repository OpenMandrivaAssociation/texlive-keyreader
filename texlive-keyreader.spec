Name:		texlive-keyreader
Version:	28195
Release:	2
Summary:	A robust interface to xkeyval
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keyreader
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyreader.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyreader.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
