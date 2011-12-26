# revision 24912
# category Package
# catalog-ctan /macros/latex/contrib/keyreader
# catalog-date 2011-12-22 12:42:22 +0100
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-keyreader
Version:	0.4
Release:	1
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
xkeyval, removing some of that package's restrictions and
adding the concept of complementary boolean keys. The package
addresses some of the issues now covered by the author's
ltxkeys package, which was assumed to be a replacement for
keyreader. Since the package has remained a favourite with
users, it has been reinstated.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/keyreader/keyreader-guide.cfg
%{_texmfdistdir}/tex/latex/keyreader/keyreader.sty
%doc %{_texmfdistdir}/doc/latex/keyreader/README
%doc %{_texmfdistdir}/doc/latex/keyreader/keyreader-guide.pdf
%doc %{_texmfdistdir}/doc/latex/keyreader/keyreader-guide.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
