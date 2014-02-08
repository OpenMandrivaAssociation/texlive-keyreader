# revision 25563
# category Package
# catalog-ctan /macros/latex/contrib/keyreader
# catalog-date 2012-01-19 11:04:21 +0100
# catalog-license lppl1.3
# catalog-version 0.4b
Name:		texlive-keyreader
Version:	0.4b
Release:	4
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
%{_texmfdistdir}/tex/latex/keyreader/keyreader-guide.cfg
%{_texmfdistdir}/tex/latex/keyreader/keyreader.sty
%doc %{_texmfdistdir}/doc/latex/keyreader/README
%doc %{_texmfdistdir}/doc/latex/keyreader/keyreader-guide.pdf
%doc %{_texmfdistdir}/doc/latex/keyreader/keyreader-guide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.4b-3
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4b-2
+ Revision: 783028
- Update to latest release.
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4b-1
+ Revision: 770193
- Update to latest upstream package

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4a-1
+ Revision: 758922
- Update to latest upstream release

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 745270
- texlive-keyreader
- texlive-keyreader

