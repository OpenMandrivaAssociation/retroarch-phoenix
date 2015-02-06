# The binary is stripped at linkage stage and removing -s gives
# very strange fail results
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Name:		retroarch-phoenix
Version:	20130609
Release:	2
Summary:	Simple GUI frontend for RetroArch using Phoenix framework
Group:		Emulators
License:	GPLv3
URL:		http://www.libretro.org
# git snapshot
Source0:	%{name}-%{version}.tar.bz2
# make sure proper path to libretro is set
Patch0:		retroarch-phoenix-20130318-libretro.patch
# adjust prefix and CXXFLAGS
Patch1:		retroarch-phoenix-20130318-makefile.patch
# overwrite menu-entry because the default one sucks
Patch2:		retroarch-phoenix-20130318-desktop.patch
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(sdl)
Requires:	retroarch

%description
Simple GUI frontend for RetroArch using Phoenix framework.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i s,"/usr/lib",%{_libdir},g retroarch-phoenix.cpp

%build
%setup_compile_flags
%make -f Makefile.qt

%install
%makeinstall_std -f Makefile.qt

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

