%define name	gnomoradio
%define version	0.15.1
%define release %mkrel 9

%define major	0
%define libname %mklibname %{name} %{major}

Name: 	 	%{name}
Summary: 	Finder and player of free (Creative Commons) music
Version: 	%{version}
Release: 	%{release}
Source0:	%{name}-%{version}.tar.bz2
# patches from Gentoo
Patch0:		gnomoradio-0.15.1-gcc42.patch
Patch1:		gnomoradio-0.15.1-gcc43.patch
# -------------------
Patch2:		gnomoradio-0.15.1-fix-underlinking.patch
Patch3:		gnomoradio-0.15.1-glib-single-include.patch
Patch4:		gnomoradio-0.15.1-lm.patch
URL:		http://gnomoradio.org/
License:	GPLv2+
Group:		Sound
BuildRequires:	imagemagick
BuildRequires:	libsigc++2.0-devel
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	gconfmm2.6-devel
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(ogg)
BuildRequires:  desktop-file-utils

%description
Gnomoradio is a program that can find, fetch, share, and play music that is
freely available for sharing.  The Gnomoradio project is creating an
online network where artists can promote and share their music freely and
willingly. By eliminating many of the exclusionary tactics of the mainstream
music industry, musicians now have a chance to interact directly with their
listeners and receive valuable exposure.

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%{name}-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure2_5x
%make LIBS="-lglibmm-2.4 -lsigc-2.0"
										
%install
%makeinstall

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --add-category="AudioVideo" \
  --add-category="Audio" \
  --add-category="Player" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}/%{_liconsdir}
convert -size 48x48 %{name}/%{name}.png %{buildroot}/%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}
convert -size 32x32 %{name}/%{name}.png %{buildroot}/%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_miconsdir}
convert -size 16x16 %{name}/%{name}.png %{buildroot}/%{_miconsdir}/%{name}.png

#%find_lang %{name}

%files 
#-f %{name}.lang
%doc AUTHORS README NEWS TODO
%{_bindir}/%{name}
%{_bindir}/rainbow-get
%{_sbindir}/rainbow-hub
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libname}-devel
%{_includedir}/rainbow
%{_includedir}/roboradio
%{_libdir}/*.so
