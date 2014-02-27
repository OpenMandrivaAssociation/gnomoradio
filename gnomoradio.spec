%define major 0
%define libroboradio %mklibname roboradio %{major}
%define librainbow %mklibname rainbow %{major}
%define libaudio %mklibname %{name}-audio %{major}
%define libmp3 %mklibname %{name}-mp3 %{major}
%define devname %mklibname %{name} -d

Summary:	Finder and player of free (Creative Commons) music
Name:		gnomoradio
Version:	0.15.1
Release:	10
License:	GPLv2+
Group:		Sound
Url:		http://gnomoradio.org/
Source0:	%{name}-%{version}.tar.bz2
# patches from Gentoo
Patch0:		gnomoradio-0.15.1-gcc42.patch
Patch1:		gnomoradio-0.15.1-gcc43.patch
# -------------------
Patch2:		gnomoradio-0.15.1-fix-underlinking.patch
Patch3:		gnomoradio-0.15.1-glib-single-include.patch
Patch4:		gnomoradio-0.15.1-lm.patch
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(gconfmm-2.6)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libxml++-2.6)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)

%description
Gnomoradio is a program that can find, fetch, share, and play music that is
freely available for sharing. The Gnomoradio project is creating an
online network where artists can promote and share their music freely and
willingly. By eliminating many of the exclusionary tactics of the mainstream
music industry, musicians now have a chance to interact directly with their
listeners and receive valuable exposure.

%files
%doc AUTHORS README NEWS TODO
%{_bindir}/%{name}
%{_bindir}/rainbow-get
%{_sbindir}/rainbow-hub
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

#----------------------------------------------------------------------------

%package -n %{libroboradio}
Summary:	Dynamic library from %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gnomoradio0 < 0.15.1-10
Obsoletes:	%{_lib}gnomoradio0 < 0.15.1-10

%description -n %{libroboradio}
Dynamic library from %{name}.

%files -n %{libroboradio}
%{_libdir}/libroboradio.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{librainbow}
Summary:	Dynamic library from %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gnomoradio0 < 0.15.1-10

%description -n %{librainbow}
Dynamic library from %{name}.

%files -n %{librainbow}
%{_libdir}/librainbow.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libaudio}
Summary:	Dynamic library from %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gnomoradio0 < 0.15.1-10

%description -n %{libaudio}
Dynamic library from %{name}.

%files -n %{libaudio}
%{_libdir}/libroboradio-audio.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libmp3}
Summary:	Dynamic library from %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gnomoradio0 < 0.15.1-10

%description -n %{libmp3}
Dynamic library from %{name}.

%files -n %{libmp3}
%{_libdir}/libroboradio-mp3.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libroboradio} = %{EVRD}
Requires:	%{librainbow} = %{EVRD}
Requires:	%{libaudio} = %{EVRD}
Requires:	%{libmp3} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}gnomoradio0-devel < 0.15.1-10

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%files -n %{devname}
%{_includedir}/rainbow
%{_includedir}/roboradio
%{_libdir}/*.so

#----------------------------------------------------------------------------

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
%makeinstall_std

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="GTK" \
	--add-category="AudioVideo" \
	--add-category="Audio" \
	--add-category="Player" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

mkdir -p %{buildroot}/%{_liconsdir}
convert -size 48x48 %{name}/%{name}.png %{buildroot}/%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}
convert -size 32x32 %{name}/%{name}.png %{buildroot}/%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_miconsdir}
convert -size 16x16 %{name}/%{name}.png %{buildroot}/%{_miconsdir}/%{name}.png

