# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/stack
# catalog-date 2007-02-28 00:02:05 +0100
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-stack
Version:	1.00
Release:	1
Summary:	Tools to define and use stacks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stack
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stack.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stack.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a small set of commands to implement
stacks independently of TeX's own stack. As an example of how
the stacks might be used, the documentation offers a small
"relinput" package that implements the backbone of the import
package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stack/relinput.sty
%{_texmfdistdir}/tex/latex/stack/stack.sty
#- source
%doc %{_texmfdistdir}/source/latex/stack/stack.dtx
%doc %{_texmfdistdir}/source/latex/stack/stack.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
