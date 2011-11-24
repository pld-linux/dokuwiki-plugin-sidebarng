%define		plugin	sidebarng
Summary:	Adds flexible sidebar to DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20100604
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://cloud.github.com/downloads/chimeric/dokuwiki-plugin-sidebarng/plugin-sidebarng.tgz
# Source0-md5:	918b55089ebcbb8c98bd3b08f79aad37
URL:		http://www.dokuwiki.org/template:sidebar
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	dokuwiki >= 20091225
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Better navigation with DokuWiki. Features a navigation sidebar, a
tagline, highlighting the current page in the sidebar (unique
feature!), using the page heading as link text automatically. Retains
the default DokuWiki look and feel as much as possible.

%description -l pl.UTF-8
Lepsza nawigacja przy użyciu DokuWiki. Opiera się na sidebarze
nawigacyjnym, pasku podświetlającym aktualną stronę na sidebarze (co
jest unikalną cechą!), przy automatycznym użyciu nagłówka strony jako
tekstu odnośnika. Zachowuje domyślny wygląd i zachowanie DokuWiki na
ile to możliwe.

%prep
%setup -qc
mv %{plugin}/* .

version=$(cat VERSION)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
#	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.css
%{plugindir}/*.php
%{plugindir}/conf
%{plugindir}/sidebars
